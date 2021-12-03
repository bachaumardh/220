class SalesForce:

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        file_read = open(file_name, 'r')
        line = file_read.readlines()
        self.sales_people.append(line)

    def quota_report(self, quota):
        file_read = open('salesData.txt', 'r')
        line = file_read.readlines()
        for i in range(len(line)):
            new_line = line[i].split()
            name = new_line[1:3]
            separate = ", "
            name = separate.join(name)
            name = name[:-1]
            employee_id = new_line[0]
            employee_id = employee_id[:-1]
            employee_id = int(employee_id)
            total = 0
            numbers = new_line[3:]
            for sales in range(len(numbers)):
                x = float(numbers[sales])
                total += x
            quo = False
            if total >= quota:
                quo = True

            x = [employee_id, name, total, quo]
            print(x)

    def top_seller(self):
        file_read = open('salesData.txt', 'r')
        line = file_read.readlines()
        total_list = []
        self.sales_people.append(line)
        for i in range(len(line)):
            new_line = line[i].split()
            total = 0
            numbers = new_line[3:]

            for sales in range(len(numbers)):
                x = float(numbers[sales])
                s = int(x)
                total += s
            total_list.append(total)

        for j in range(len(total_list)):
            if total_list[j] >= max(total_list):
                print(new_line)

    def individual_sales(self, employee_id):
        file_read = open('salesData.txt', 'r')
        line = file_read.readlines()
        for i in range(len(line)):
            new_line = line[i].split()
            emp_id = new_line[0]
            new_id = emp_id[0:-1]
            new = int(new_id)
            if employee_id == new:
                print(new_line)
            elif employee_id != new:
                print('None')
                break



