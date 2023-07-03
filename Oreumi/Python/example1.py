class HealthCheck:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def check_health(self):
        bmi = self.calculate_bmi()
        result = self.get_result(bmi)

        print("=== 건강검진 결과 ===")
        print(f"이름: {self.name}")
        print(f"나이: {self.age}")
        print(f"신장: {self.height}cm")
        print(f"체중: {self.weight}kg")
        print(f"BMI: {bmi:.2f}")
        print(f"결과: {result}")

    def calculate_bmi(self):
        height_in_meters = self.height / 100
        bmi = self.weight / (height_in_meters ** 2)
        return bmi

    def get_result(self, bmi):
        if bmi < 18.5:
            return "저체중"
        elif 18.5 <= bmi < 23:
            return "정상체중"
        elif 23 <= bmi < 25:
            return "과체중"
        elif 25 <= bmi < 30:
            return "경도비만"
        else:
            return "고도비만"
        
    def backup_records(self):
        file_path = "backup.txt"
        with open(file_path, 'w', encoding="utf-8") as file:
            file.write("=== 건강검진 결과 ===\n")
            file.write(f"이름: {self.name}\n")
            file.write(f"나이: {self.age}\n")
            file.write(f"신장: {self.height}cm\n")
            file.write(f"체중: {self.weight}kg\n")
            file.write(f"BMI: {self.calculate_bmi()}\n")
            file.write(f"결과: {self.get_result(self.calculate_bmi())}\n")
        

my_patient1 = HealthCheck("이원일", 26, 180, 70)
my_patient2 = HealthCheck("이원이", 18, 180, 70)
my_patient3 = HealthCheck("이원삼", 42, 180, 70)
my_patient4 = HealthCheck("이원사", 34, 180, 70)
my_patient5 = HealthCheck("이원오", 25, 180, 70)

patients = [my_patient1,my_patient2,my_patient3,my_patient4,my_patient5]
avg = 0
for p in patients:
    avg+=p.age

avg/=len(patients)