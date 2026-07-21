import { useState } from "react"
import Header from "./components/Header"
import data from "./data"
function App(){
   const [counter,setCounter] = useState(100)
   const [studentList,setStudentList] = useState(data)
   const incrementCounter = ()=>{
    //window.alert("Function called...")
    //counter = counter + 1
    setCounter(counter+1)
   }
   const deleteStudent = (id)=>{
     if(window.confirm("Do you want to delete ?")){
      let index = studentList.findIndex((student)=>{return student.id == id})
      studentList.splice(index,1)
      setStudentList([...studentList])
     }
   
  }
   return <>
     <h1>App component....</h1>
     <Header/>
     <h1>Counter : {counter}</h1>
     <button onClick={incrementCounter}>Increment counter</button>
     <table border="1" width="100%">
      <tr>
        <td>Id</td>
        <td>Name</td>
        <td>Roll</td>
        <td>Per.</td>
        <td>Course</td>
        <td>Delete</td>
      </tr>
      {studentList.map((student,index)=>{return <tr key={student.id}>
        <td>{student.id}</td>
        <td>{student.name}</td>
        <td>{student.roll}</td>
        <td>{student.per}</td>
        <td>{student.course}</td>
        <td>
          <button onClick={()=>{deleteStudent(student.id)}}>Delete</button>
        </td>
      </tr>})}
     </table>
   </> 
}

export default App