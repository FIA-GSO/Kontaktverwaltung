#
# f.folkmann@gso.schule.koeln, 2022
#
"""contact class definition"""
class Contact:
   def __init__(self, firstname, lastname):
      """construction"""
      self.firstname = firstname
      self.lastname = lastname

   def __str__(self):
      """display string"""
      return f"{self.lastname}, {self.firstname}".rstrip(' ,')

   def to_dict(self):
      """get object state as dictionary"""
      return self.__dict__

   def from_dict(dict):
      """creates a contact from given dictionary"""
      return Contact(
         dict["firstname"],
         dict["lastname"])

if __name__ == "__main__":
    #test code here
    pass
