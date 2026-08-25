import React from "react"

function First({sayHello}){
    console.log("First Render....")
    return <>
      <h1>First Component...</h1>
      <button onClick={sayHello}>Say Hello</button>
    </>
}

export default React.memo(First);