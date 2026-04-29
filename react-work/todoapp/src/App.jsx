import { useRef, useState } from "react";
import ToDoData from "./ToDoData";
function App(){
  const [taskList,setTaskList] = useState(ToDoData);
  const [priorityList,setPriorityList] = useState([
    {"priorityId":1, "priorityValue":"Low"},
    {"priorityId":2, "priorityValue":"Normal"},
    {"priorityId":3, "priorityValue":"High"}
  ]);
  const [statusFilter,setStatusFilter] = useState("active");
  
  let titleRef = useRef(null);
  let priorityRef = useRef(null);

  const addTask = ()=>{
    let title = titleRef.current.value;
    let pid = priorityRef.current.value;
    let date = new Date();
    date = date.getDate()+"/"+(date.getMonth()+1)+"/"+date.getFullYear();
    let status = "active";
    let newTask = {title,pid,date,status};
    setTaskList([...taskList,newTask]);
  } 
  const changeStatus = (task,newStatus)=>{
    let index =  taskList.findIndex((obj)=>{return obj.title == task.title});
    taskList.splice(index,1);
    task.status = newStatus;
    taskList.splice(index,0,task);
    setTaskList([...taskList]);
  }
  return <>
    <div className="bg-danger p-2 text-center">
      <span className="text-white">To-Do App</span>
    </div>
    <div className="container mt-3 mb-3">
      <div className="row">
        <div className="col-md-6">
          <input ref={titleRef} className="form-control" placeholder="Enter task title"/>
        </div>
        <div className="col-md-6">
          <select ref={priorityRef} className="form-control">
            <option>select priority</option>
            {priorityList.map((pObj,index)=>{return <option key={pObj.priorityId} value={pObj.priorityId}>{pObj.priorityValue}</option>})}
          </select>
        </div>
      </div>
      <div className="row mt-2">
        <div className="col-md-6">
            <button onClick={addTask} className="btn btn-success">ADD</button>
        </div>
      </div>
    </div>
    <div className="container mt-3">
      <div className="mt-2 mb-2">
        <button disabled={statusFilter=="active" ? true: false} onClick={()=>setStatusFilter("active")} className="btn btn-success">Active({taskList.filter((task)=>{return task.status == "active"}).length})</button>
        <button disabled={statusFilter=="deactive" ? true : false} onClick={()=>setStatusFilter("deactive")} className="btn btn-danger ml-2">Deactive({taskList.filter((task)=>{return task.status=="deactive"}).length})</button>
      </div>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>S.no</th>
            <th>Title</th>
            <th>Date</th>
            <th>Priority</th>
            <th>Change Status</th>
          </tr>
        </thead>
        <tbody>
          {taskList.filter((task)=>{return task.status == statusFilter}).sort((a,b)=>{return b.pid-a.pid}).map((task,index)=>{return <tr className={task.pid==1? "bg-success" : task.pid==2 ? "bg-warning" : "bg-danger"} key={index}>
            <td>{index+1}</td>
            <td>{task.title}</td>
            <td>{task.date}</td>
            <td>{priorityList.find((pObj)=>{return pObj.priorityId == task.pid}).priorityValue}</td>
            <td>
              {task.status=="active" ? <button className="btn btn-outline-secondary" onClick={()=>{changeStatus(task,"deactive")}}>Deactive</button> : <button onClick={()=>{changeStatus(task,"active")}} className="btn btn-outline-secondary">Active</button>}
            </td>
          </tr>})}
        </tbody>
      </table>
    </div>
  </>
}

export default App;