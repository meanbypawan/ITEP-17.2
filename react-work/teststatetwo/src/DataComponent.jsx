import { Component } from "react";
import Data from "./Data";
class DataComponent extends Component{
    constructor(){
        super();
        this.state = {
            recipeList: Data
        }
    }
    render(){
        console.log(this.state.recipeList);
        return <>
          <h1>Data Component...</h1>
          <table border='1' width="100%">
            <tr>
                <td>Name</td>
                <td>Image</td>
                <td>Difficulty</td>
                <td>Cook Time</td>
            </tr>
            {this.state.recipeList.map((obj,index)=>{return <tr key={obj.id}>
                <td>{obj.name}</td>
                <td>
                    <img src={obj.image} width="70px" height="70px"/>
                </td>
                <td>{obj.difficulty}</td>
                <td>{obj.cookTimeMinutes}</td>
            </tr>})}
          </table>
        </>
    }
}

export default DataComponent;