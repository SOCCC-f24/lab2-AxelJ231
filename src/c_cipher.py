import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Axel Jackson 10/23/24 CSC-138 
 
def encrypt(email="abc012"):
    """
    TODO: The objective is to create a function that can encrypt a 6 character long email. 

    Args:
        TODO:  The argument is an email that is a string. 

    Returns:
        TODO: retVal is going to be returned and it is a string data type  
    """
    output = "" 
    len_flag = len(email) != 6
    # TODO: fix line below and, implement functionality rather than literals
    # keep all updates in the anum_flag (bool) variable
    # i.e., 
    #     A = email[:3] (check first half)
    #     B = email[3:] (check second half)
    #     anum_flag = A or B
    anum_flag = not((email[:3]).isalpha()) or not((email[3:]).isdecimal()) 

    if len_flag:                         # NOTE: here we provide input validation on length
        output = "Length check failed\n"
        output += "Email must be 6 characters long."
        logging.info(output)
        return output        
    if anum_flag:                        # NOTE: here we provide input validation on alpha/num
        output = "alpha num check failed\n"
        output += "Email must have 3 letters followed by 3 digits."
        logging.info(output)
        return output     
        
    # TODO: fix line below, process our string into a list
    email_lst = list(email)
        
    # TODO: complete line(s) below, convert EACH new element into a string
    new_ascii = []
    for elem in email_lst: # NOTE: here we extract and update element at 0 
        new_ascii.append(ord(elem) + 3)
        
    for index, elem in enumerate(new_ascii):  # NOTE: here we convert our ASCII into string
        email_lst[index] = chr(elem)  
        
    # TODO: fix line below, convert list into a string
    email_str = "".join(email_lst)

    # keep all updates in the retVal (str) variablei
    # i.e.,
    #    email_str = " some string updates here "
    #    email_1 = email_str.strip()
    #    retVal = email_1
    retVal = email_str
    return retVal 

def decrypt(email="def345"):
    """
    TODO: The objective is to take an encrypted email and decrypt it. 

    Args:
        TODO: The input should be an encrypted email. This email will be in the form of a string.

    Returns:
        TODO: The returned variable will be retVal. It's data type is a string.   
    """
    # input validation
    output = "" 
    len_flag = len(email) != 6
    # TODO: fix line below and, implement functionality rather than literals
    # keep all updates in the anum_flag (bool) variable
    # i.e., 
    #     A = email[:3] (check first half)
    #     B = email[3:] (check second half)
    #     anum_flag = A or B
    anum_flag = not((email[:3]).isalpha()) or not((email[3:]).isdecimal()) 

    if len_flag:                         # NOTE: here we provide input validation on length
        output = "Length check failed\n"
        output += "Email must be 6 characters long."
        logging.info(output)
        return output        
    if anum_flag:                        # NOTE: here we provide input validation on alpha/num
        output = "alpha num check failed\n"
        output += "Email must have 3 letters followed by 3 digits."
        logging.info(output)
        return output     
        
    # TODO: fix line below, process our string into a list
    email_lst = list(email)
        
    # TODO: complete line(s) below, convert EACH new element into a string
    new_ascii = []
    for elem in email_lst: # NOTE: here we extract and update element at 0 
        new_ascii.append(ord(elem) - 3)
        
    for index, elem in enumerate(new_ascii):  # NOTE: here we convert our ASCII into string
        email_lst[index] = chr(elem)  
        
    # TODO: fix line below, convert list into a string
    email_str = "".join(email_lst)

    # keep all updates in the retVal (str) variablei
    # i.e.,
    #    email_str = " some string updates here "
    #    email_1 = email_str.strip()
    #    retVal = email_1
    retVal = email_str
    return retVal 
