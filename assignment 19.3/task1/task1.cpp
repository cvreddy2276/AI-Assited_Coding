#include <string>

class Student {
private:
    std::string name;
    int age;
    int grade; // 0 - 100

public:
    // Constructor
    Student(const std::string& name, int age, int grade)
        : name(name), age(age), grade(grade) {
    }

    // Accessor
    int getGrade() const {
        return grade;
    }

    // Optional: other accessors if needed
    const std::string& getName() const {
        return name;
    }

    int getAge() const {
        return age;
    }
};