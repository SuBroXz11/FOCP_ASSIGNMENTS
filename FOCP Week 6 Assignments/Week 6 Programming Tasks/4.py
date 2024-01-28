# def simple_encrypt(message):
#     # Remove spaces from the message
#     message_without_spaces = message.replace(" ", "")
    
#     # Reverse the string
#     encrypted_message = message_without_spaces[::-1]
    
#     return encrypted_message

# # Test the function
# original_message = "Hello, World! This is a simple encryption example."
# encrypted_message = simple_encrypt(original_message)

# print(f"Original Message: {original_message}")
# print(f"Encrypted Message: {encrypted_message}")

def enc(msg):
    no_space_msg="".join(msg.split(" "))
    encry_msg=no_space_msg[::-1]
    return encry_msg

orgi_msg="hello world"
print(enc(orgi_msg))