string_object = "Hello user ! < this first object str()"

print( string_object )
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if "Hello" in string_object:
    print("Object have 'Hello'")
else:
    print(string_object , "== type str")
# -------------------------------------------
print("============================================")
# ==========================================================================

name_user = "Admin 1233123123"
print("Object create!!! type (str)")
print(name_user)
print("============================================")

if "Admin" in name_user:
    print("Sorry object not verify")
elif "123" in name_user:
    print("Please non create type int ")