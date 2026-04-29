import { Component } from "react";
import StudentArray from "./Data";
class App extends Component{
  constructor(){
    super();
    this.state = {
      studentList: StudentArray,
      branchList: ["CS","IT","CV","MECH"],
      branchFilter: "All"
    }
  }
  addStudent = ()=>{
     let roll = this.rollInput.value;
     let name = this.nameInput.value;
     let branch = this.branchInput.value;
     let gender = this.genderInput.value;
     let newStudent = {roll,name,branch,gender};
     this.setState({studentList:[...this.state.studentList,newStudent]});
  }
  render(){
    return <>
      <div className="bg-danger p-1">
        <h5 className="text-white text-center">Student App</h5>
      </div>
      <div className="container mt-3 mb-3">
        <div className="row">
          <div className="col-md-6">
            <input ref={(rollInputObj)=>{this.rollInput=rollInputObj}} id="rollInput" type="text" placeholder="Enter student roll number" className="form-control"/>
          </div>
          <div className="col-md-6">
            <input ref={(nameInputObj)=>{this.nameInput = nameInputObj}} id="nameInput" type="text" placeholder="Enter student name" className="form-control"/>
          </div>
        </div>
        <div className="row mt-2">
          <div className="col-md-6">
            <select ref={(branchInputObj)=>this.branchInput = branchInputObj} id="branchInput" className="form-control">
              <option>Select branch</option>
              {this.state.branchList.map((branch,index)=>{return <option key={branch}>{branch}</option>})}
            </select>
          </div>
          <div className="col-md-6">
            <select ref={(genderInoutObj)=>this.genderInput = genderInoutObj} id="genderInput" className="form-control">
              <option>Select gender</option>
              <option>Male</option>
              <option>Female</option>
            </select>
          </div>
        </div>
        <div className="row mt-2">
          <div className="col-md-6">
            <button onClick={this.addStudent} className="btn btn-success">ADD</button>
          </div>
          <div className="col-md-6">
            <button onClick={()=>{this.setState({branchFilter:"CS"})}} className="ml-2 btn btn-info">CS({this.state.studentList.filter((student)=>{return student.branch=="CS"}).length})</button>
            <button onClick={()=>{this.setState({branchFilter:"IT"})}} className="ml-2 btn btn-danger">IT({this.state.studentList.filter((student)=>{return student.branch=="IT"}).length})</button>
            <button onClick={()=>{this.setState({branchFilter:"CV"})}} className="ml-2 btn btn-primary">CV({this.state.studentList.filter((student)=>{return student.branch=="CV"}).length})</button>
            <button onClick={()=>{this.setState({branchFilter:"MECH"})}} className="ml-2 btn btn-warning">MECH({this.state.studentList.filter((student)=>{return student.branch=="MECH"}).length})</button>
            <button onClick={()=>{this.setState({branchFilter:"All"})}} className="ml-2 btn btn-secondary">Total({this.state.studentList.length})</button>
          </div>
        </div>
      </div>
      <table className="table table-striped">
         <thead>
          <tr>
            <th>S.no</th>
            <th>Roll number</th>
            <th>Name</th>
            <th>Gender</th>
            <th>Branch</th>
            <th>Remove</th>
          </tr>
         </thead>
         <tbody>
          {this.state.studentList.filter((student)=>{return this.state.branchFilter=="All" || student.branch == this.state.branchFilter}).map((student,index)=>{return <tr key={index}>
            <td>{index+1}</td>
            <td>{student.roll}</td>
            <td>{student.name}</td>
            <td>{student.gender}</td>
            <td>{student.branch}</td>
            <td>
              <button className="btn btn-outline-danger">Remove</button>
            </td>
          </tr>})}
         </tbody>
      </table>
    </>
  }
}

export default App;