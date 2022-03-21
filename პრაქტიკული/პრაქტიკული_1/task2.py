class TestPaper:

    def __init__(self, subject: str, test_scheme: list, pass_mark: str):
        self.subject = subject
        self.test_scheme = test_scheme
        self.pass_mark = pass_mark


class Student:

    def __init__(self, tests_taken="No tests Taken"):
        self.tests_taken = tests_taken

    def take_test(self, taken_test: TestPaper, student_answers: list):

        # ვქმნი ორ ცვლადს რომელიც გათვალისწინებული სტუდენდის მიერ დაწერილი ტესტის სწორი პასუხებისა და სწორი პასუხების
        # პროცენტული მაჩვენებლისთვის
        correct_answers = 0
        correct_answers_percentage = 0

        # ინტერვლაში(რამდენი საკითხიცაა ტესტში) ვადარებ მოსწავლის პასუხებსა და სწორ პასუხებს, სწორს პასუხების
        # რაოდენობას კი უშუალოდ ზემოთ აღნიშნულ ცვლადში ვინახავ
        for answer in range(len(student_answers)):
            if taken_test.test_scheme[answer] == student_answers[answer]:
                correct_answers += 1

        # ცვლადს(სწორი პასუხების პროცენტული მაჩვენელი) მათემატიკური გარდაქმნით, ვანიჭებ დამრგვალებულ პროცენტულ
        # მაჩვენებლს სწორი პასუხებისა
        correct_answers_percentage = round((correct_answers / len(student_answers)) * 100)

        # რადგან default პარამეტრად string ობიექცია დაწერილი ტესტები ,ვცდილობ იგი გარდავაქმნა dictionary ობიექტად,
        # სადაც შემდგომ ჩიაწერება საგანი და შესაბამისი პროცენტული მაჩვენელი
        if type(self.tests_taken) == str:
            self.tests_taken = {}

        # იმ შემთხვევაში თუ სტუდენტმა გადალახა ბარიერი,რომელიც მოცემული იყპ ტესტში,მაშინ მის აქტივში ჩაიწერება
        # გადალახული, წინააღმდეგ შემთხვევაში კი იგი ჩაიჭრება
        if correct_answers_percentage >= int(taken_test.pass_mark.rstrip('%')):
            self.tests_taken[taken_test.subject] = f"Passed! ({correct_answers_percentage})"
        else:
            self.tests_taken[taken_test.subject] = f"Failed! ({correct_answers_percentage})"


paper1 = TestPaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
paper2 = TestPaper("Chemistry", ["1C", "2D", "3C", "4B", "5A", "6A"], "70%")

student1 = Student()

print(student1.tests_taken)
student1.take_test(paper1, ["1A", "2C", "3D", "4A", "5A"])

student1.take_test(paper2, ["1C", "2D", "3C", "4C", "5A", "6D"])
print(student1.tests_taken)
