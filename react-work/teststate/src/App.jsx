import { Component } from "react";
import TestBinding from "./TestBinding";
class App extends Component{
   constructor(){
    super();
    this.state = {
      counter: 100,
      evenCounter: 0
    };
   }
   increment = ()=>{
    this.setState({counter: this.state.counter + 1});
   }
   incrementEvenCounter = ()=>{
     this.setState({evenCounter: this.state.evenCounter + 2});
   }
   render(){
    console.log("Component Re-renders");
    let message = "ReactJs is simple...";
    return <>
       <h1>App Component....</h1>
       <hr/>
       <h1>{this.state.counter} : {this.state.evenCounter}</h1>
       <button onClick={this.increment}>Increment Counter...</button>
       <button onClick={this.incrementEvenCounter}>Even Counter</button>
       <h2>{message}</h2>
       <h3>{20+10}</h3>
       <TestBinding/>
    </>
   }
}
export default App;