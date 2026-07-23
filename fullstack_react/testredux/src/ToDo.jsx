import { useEffect } from "react"
import { useSelector } from "react-redux"

function ToDo(){
    const {todos} = useSelector((store)=>store.ToDos)
    return <>
       <table border="1" width="100%">
         <tr>
            <td>Id</td>
            <td>ToDo</td>
            <td>Completed</td>
            <td>UserId</td>
         </tr>
         {todos?.map((todoItem,index)=>{return <tr key={todoItem.id}>
            <td>{todoItem.id}</td>
            <td>{todoItem.todo}</td>
            <td>{todoItem.completed}</td>
            <td>{todoItem.userId}</td>
         </tr>})}
       </table>
    </>
}

export default ToDo