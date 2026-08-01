import React from "react"
function Third({wishingMessage}){
    console.log("Third Rerender....")
    return <>
      <h1>Third Component...</h1>
      {wishingMessage.m1} : {wishingMessage.m2} : {wishingMessage.evenCounter}
    </>
}

export default React.memo(Third)