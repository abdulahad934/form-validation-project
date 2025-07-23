class Form:
    def __init__(self, name, userName, password, email, age, phone):
        self.name = name
        self.userName = userName
        self.password = password
        self.email = email
        self.age = age
        self.phone = phone
        
    def user_info(self):
        name = self.name.strip()
        parts = name.split()
        
        if len(parts) < 2:
            
           
            
            return "Invalid name format. Please provide at least 5 parts."
        elif len(self.userName) < 5:
            return "UserName must be at least 5 characters long."
        elif len(self.password) < 5:
            return "Password must be at least 5 characters long."
        elif '@' not in self.email or '.com' not in self.email:
            return "Email must contain '@' and end with '.com'."
        elif not self.age.isdigit() or int(self.age) < 18:
            return "Age must be a number and at least 18."
        elif not self.phone.isdigit() or len(self.phone) !=11:
            return "Phone number must be 11 digits long and contain only numbers."
        else:
            first = parts[0].capitalize()
            last = parts[1].capitalize()
            return f"User Info: {first} {last}, Username: {self.userName}, Email:{self.email}, Age: {self.age}, Phone: {self.phone}"   

    def validate(self):
        return self.user_info()


form = Form("abdulahada hadashikurrahman ", "abdulahad", "password123", "abdulahad@.com", "20", "12345678901")

print(form.validate())
                         
            