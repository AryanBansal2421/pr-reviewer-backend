from backend.agents.security_agent import security_agent
from backend.agents.quality_agent import quality_agent
from backend.agents.architect_agent import architect_agent

# Fake diff for testing
test_diff = """
diff --git a/app.py b/app.py
index 1234567..abcdefg 100644
--- a/app.py
+++ b/app.py
@@ -1,10 +1,15 @@
+import os
+password = "admin123"
+api_key = "sk-1234567890abcdef"
+
 def get_users(user_id):
-    query = "SELECT * FROM users WHERE id = " + user_id
+    query = f"SELECT * FROM users WHERE id = {user_id}"
     return db.execute(query)
+
+def calculate(n):
+    result = []
+    for i in range(n):
+        for j in range(n):
+            result.append(i*j)
+    return result
"""

print("Testing Security Agent...")
print(security_agent(test_diff))
print("\n" + "="*50 + "\n")

print("Testing Quality Agent...")
print(quality_agent(test_diff))
print("\n" + "="*50 + "\n")

print("Testing Architect Agent...")
print(architect_agent(test_diff))
