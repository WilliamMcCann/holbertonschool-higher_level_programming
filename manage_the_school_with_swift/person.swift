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

class Mentor: Person, Classify {
    func isStudent() -> Bool {
    return false
    }
}

class Student: Person, Classify {
    func isStudent() -> Bool {
    return true
    }
}
