// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.5.0 <0.9.0;


contract Student_Management{
struct Student{
    string name;
    uint age;
    string enrollmentStatus;
    uint[] grades;
}
mapping(uint => Student) public students;
uint[] public studentIds;

constructor(string memory _name, uint _age, string memory _enrollmentStatus, uint[] memory _grades)public {

    students[1] = Student(_name,_age,_enrollmentStatus,_grades);

    studentIds.push(1);
}

function addStudent(string memory _name, uint _age, string memory _enrollmentStatus, uint[] memory _grades) public {

    uint newID = studentIds.length + 1;
    students[newID] =

    Student(_name,_age,_enrollmentStatus,_grades);

    studentIds.push(newID);
}
function updateStudentInfo(uint ID, string memory _enrollmentStatus) public {
    uint validity = 0;
    for(uint i =0; i < studentIds.length;i++){
        if(studentIds[i] == ID){
            validity = 1;
            }
        }
    require(validity != 0, "Student does not exist!");
    students[ID].enrollmentStatus = _enrollmentStatus;

    }

function getStudents(uint StudentID) public view returns(string memory,uint,string memory,uint[] memory){

    uint validity = 0;
    for(uint i =0; i < studentIds.length;i++){
        if(studentIds[i] == StudentID){
            validity = 1;
        }
    }
    require(validity != 0, "Student does not exist!");
    Student memory student = students[StudentID];

    return(student.name,student.age,student.enrollmentStatus,student.grades);
}

function updateStudentAge(uint ID, uint _age) public {
    uint validity = 0;
    for(uint i =0; i < studentIds.length;i++){
        if(studentIds[i] == ID){
            validity = 1;
        }
    }
    require(validity != 0, "Student does not exist!");
    students[ID].age = _age;

    }
}