import { Component, PureComponent } from "react";

class Home extends PureComponent{
    constructor(){
        super();
        console.log("Home Constructor called...");
    }
    componentDidMount(){
        console.log("Home Component Mount....");
    }
    componentDidUpdate(){
        console.log("Home compoenent Update....");
    }
    componentWillUnmount(){
        console.log("Home Component Unmount...");
    }
    render(){
        console.log("Home Render()");
        return <>
          <h3>Home Component...</h3>
          <hr/>
        </>
    }
}

export default Home;