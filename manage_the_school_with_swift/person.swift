class Person {

    //Public attributes
    var first_name : String
    var last_name : String
    var age : Int

    //Public methods
    init(first_name: String, last_name: String, age: Int) {
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    }

    func fullName() -> String{
        return "\(first_name) \(last_name)"
    }
}

//Protocol
protocol Classify{
    func isStudent() -> Bool
}

//Enumeration
enum Subject {
    case Math
    case English
    case French
    case History
}

class Mentor: Person, Classify {
    init(first_name: String, last_name: String, age: Int, subject: Subject = Subject.Math) {
        self.subject = subject
        super.init(first_name: first_name, last_name: last_name, age: age)
    }


    func isStudent() -> Bool {
    return false
    }

    let subject: Subject

    func stringSubject() -> String {
        switch self.subject {
            case Subject.Math:
                return "Math"
            case Subject.English:
                return "English"
            case Subject.French:
                return "French"
            case Subject.History:
                return "History"
        }
    }
}

class Student: Person, Classify {
    func isStudent() -> Bool {
    return true
    }
}
