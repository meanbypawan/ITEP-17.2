import { Component } from "react"

class TestBinding extends Component{
    constructor(){
        super();
        this.cssList = {
        greenColor:{
            color: "green"
        },
        redColor:{
            color: "red"
        }
        }
    }
    render(){
        let fruitList = ["Mango","Banana","Strawberry","Apple","Orange"];
        return <>
          <h1 style={{color: "blue", fontSize:"20px", fontStyle:"italic"}}>Test Binding Component...</h1>
          <ol>
           {fruitList.map((element,index)=>{
            return <li style={index%2 ? this.cssList.greenColor : this.cssList.redColor} key={element}>{element}</li>})}
          </ol>
        </>
    }
}

export default TestBinding;