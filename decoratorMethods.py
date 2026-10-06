# ==============================================================================
# REAL-WORLD SOFTWARE EXAMPLE: A USER AUTHENTICATION & PROFILE SYSTEM
# ==============================================================================
# This single script demonstrates the exact real-world differences between:
# 1. Regular Instance Methods (Needs a specific user)
# 2. Class Methods (@classmethod) (Acts as a shortcut factory to create users)
# 3. Static Methods (@staticmethod) (Isolated helper tool that needs no user data)
# ==============================================================================

import json

class UserProfile:
    # Class-level variable shared across the entire system
    COMPANY_DOMAIN = "techcorp.com"

    def __init__(self, username, email, role):
        self.username = username    # Instance variable
        self.email = email          # Instance variable
        self.role = role            # Instance variable

    # --------------------------------------------------------------------------
    # 1. REGULAR INSTANCE METHOD
    # --------------------------------------------------------------------------
    # Use Case: Operating on a specific user account that already exists.
    # It requires 'self' to read or modify that specific user's properties.
    def get_dashboard_permissions(self):
        if self.role == "Admin":
            return f"ACCESS GRANTED: {self.username} has full system controls."
        else:
            return f"ACCESS RESTRICTED: {self.username} has standard read-only view."


    # --------------------------------------------------------------------------
    # 2. CLASS METHOD (@classmethod)
    # --------------------------------------------------------------------------
    # Use Case: A factory shortcut to build a new UserProfile object.
    # It receives 'cls' (the class itself) to construct and return a new instance.
    # This is incredibly useful for parsing JSON data from a database or API.
    @classmethod
    def from_database_json(cls, json_string):
        # Parse the raw network string into a Python dictionary
        data = json.loads(json_string)
        
        # We auto-generate the professional email using the class domain
        generated_email = f"{data['user']}@{cls.COMPANY_DOMAIN}"
        
        # 'cls(...)' builds and returns a brand new UserProfile object!
        return cls(username=data["user"], email=generated_email, role=data["role"])


    # --------------------------------------------------------------------------
    # 3. STATIC METHOD (@staticmethod)
    # --------------------------------------------------------------------------
    # Use Case: An isolated utility tool. It does not look at 'self' or 'cls'.
    # It takes an input, processes it, and returns a result completely on its own.
    # It lives inside this class purely because password validation belongs to users.
    @staticmethod
    def is_secure_password(password):
        # A simple security check: password must be at least 8 characters long
        return len(password) >= 8


# ==============================================================================
# EXECUTION & OUTPUT VERIFICATION
# ==============================================================================
if __name__ == "__main__":
    print("--- RUNNING PROGRAM AND VERIFYING OUTPUTS ---\n")

    # --------------------------------------------------------------------------
    # PROVING 1: REGULAR METHOD (Requires an existing object)
    # --------------------------------------------------------------------------
    # We manually create a standard user object
    active_user = UserProfile("alice_dev", "alice@techcorp.com", "User")
    
    # We ask for permissions for THIS specific user
    print("[1. Regular Method Output]")
    print(active_user.get_dashboard_permissions())
    print("-" * 60 + "\n")


    # --------------------------------------------------------------------------
    # PROVING 2: CLASS METHOD (The Factory Shortcut Creator)
    # --------------------------------------------------------------------------
    # Imagine this raw JSON text came directly from a database query
    raw_db_row = '{"user": "boss_bob", "role": "Admin"}'
    
    # We call the factory shortcut directly on the class "UserProfile"
    admin_user = UserProfile.from_database_json(raw_db_row)
    
    print("[2. Class Method Output]")
    print(f"Successfully created new profile object via factory!")
    print(f"Username: {admin_user.username}")
    print(f"Generated Email: {admin_user.email}")
    print(admin_user.get_dashboard_permissions())  # Verifying the created object works
    print("-" * 60 + "\n")


    # --------------------------------------------------------------------------
    # PROVING 3: STATIC METHOD (The Independent Calculator/Tool)
    # --------------------------------------------------------------------------
    # We test a couple of passwords. Notice we don't need ANY user object to run this!
    weak_check = UserProfile.is_secure_password("12345")
    strong_check = UserProfile.is_secure_password("super_secure_999")
    
    print("[3. Static Method Output]")
    print(f"Is '12345' secure? -> {weak_check}")
    print(f"Is 'super_secure_999' secure? -> {strong_check}")
    print("-" * 60)




# --------------------------------------------------------------------------
#       4. PROPERTY (@property)
# --------------------------------------------------------------------------

"""
A complete, production-style guide to understanding the Python @property decorator.

WHAT IS A PROPERTY?
A property is a built-in decorator that transforms a method into a read-only 
attribute (variable lookalike). Coupled with `.setter`, it gives you complete 
control over how internal data is read and modified.
"""

class CloudStorageAccount:
    def __init__(self, owner: str, storage_used_gb: float):
        self.owner = owner
        
        # 1. THE CONVENTION: Leading Underscore (_)
        # The single underscore is a signal to other developers meaning:
        # "This variable is private. Do not touch or change it directly."
        self._storage_used_gb = storage_used_gb

    # =========================================================================
    # 2. THE GETTER (@property)
    # =========================================================================
    # By placing @property on top, we turn this method into a variable lookalike.
    # When a developer calls 'account.storage_used_gb', this code runs silently.
    @property
    def storage_used_gb(self):
        print(f"🔍 [LOG] Fetching storage data for {self.owner}...")
        return self._storage_used_gb

    # =========================================================================
    # 3. THE SETTER (@<property_name>.setter)
    # =========================================================================
    # When you define a @property, Python automatically makes a '.setter' available.
    # This intercepts any attempt to assign a value using an equals sign (=).
    # e.g., 'account.storage_used_gb = 50' triggers this method.
    @storage_used_gb.setter
    def storage_used_gb(self, new_amount: float):
        print(f"⚙️ [LOG] Attempting to update storage to {new_amount} GB...")
        
        # Data Validation Rule 1: Prevent negative allocation
        if new_amount < 0:
            print("❌ ERROR: Storage allocation cannot be negative.")
            return
            
        # Data Validation Rule 2: Enforce a strict maximum limit
        if new_amount > 1000:
            print("❌ ERROR: Maximum allowance exceeded! Account capped at 1000 GB.")
            return
            
        # If all rules pass, update the underlying internal variable safely
        print("✅ Success: Storage updated.")
        self._storage_used_gb = new_amount


# =============================================================================
# RUNTIME COMPILATION & EXPECTED OUTPUTS
# =============================================================================
if __name__ == "__main__":
    print("--- 📱 CREATING AN ACCOUNT ---")
    account = CloudStorageAccount(owner="DeveloperAlex", storage_used_gb=150.0)

    print("\n--- 📖 READING THE PROPERTY ---")
    # NOTICE: We DO NOT use parenthesis `()`. It looks exactly like a standard variable.
    print(f"Current Usage: {account.storage_used_gb} GB")
    # 👉 OUTPUT:
    # 🔍 [LOG] Fetching storage data for DeveloperAlex...
    # Current Usage: 150.0 GB

    print("\n--- 🛑 TRIGGERING VALIDATION 1 (NEGATIVE VALUE) ---")
    # Trying to change the variable maliciously or erroneously
    account.storage_used_gb = -50
    # 👉 OUTPUT:
    # ⚙️ [LOG] Attempting to update storage to -50 GB...
    # ❌ ERROR: Storage allocation cannot be negative.

    print("\n--- 🛑 TRIGGERING VALIDATION 2 (LIMIT EXCEEDED) ---")
    # Trying to allocate more than the system cap allows
    account.storage_used_gb = 5000
    # 👉 OUTPUT:
    # ⚙️ [LOG] Attempting to update storage to 5000 GB...
    # ❌ ERROR: Maximum allowance exceeded! Account capped at 1000 GB.

    print("\n--- ✅ SUCCESSFUL UPDATE VIA SETTER ---")
    # A legitimate system adjustment
    account.storage_used_gb = 450.0
    print(f"Confirmed Usage: {account.storage_used_gb} GB")
    # 👉 OUTPUT:
    # ⚙️ [LOG] Attempting to update storage to 450.0 GB...
    # ✅ Success: Storage updated.
    # 🔍 [LOG] Fetching storage data for DeveloperAlex...
    # Confirmed Usage: 450.0 GB


"""
Without @property, developers would have to call methods like `get_storage_used_gb()` and `set_storage_used_gb(value)`, which is less intuitive. And with the @property decorator you can access as regular attributes like `account.storage_used_gb`.
The @property decorator allows for a clean, readable interface while still enforcing encapsulation and validation rules.
"""