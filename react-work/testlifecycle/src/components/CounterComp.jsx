import { Component } from "react";

class CounterComp extends Component{
    constructor(){
        super();
        this.state = {
            counter : 10
        };
    }
    shouldComponentUpdate(nextProps,nextState){
        if(nextState.counter%2==0)
            return true;
        return false;
    }
    render(){
        console.log("Counter Component Render()");
        return <>
           <h3>Counter Component...{this.state.counter}</h3>
           <button onClick={()=>this.setState({counter: this.state.counter+1})}>Change Counter</button>
        </>
    }
}

export default CounterComp;