import React from "react"

function First(){
    console.log("First Rerender....")
    return <>
      <h2>First component...</h2>
    </>
}

export default React.memo(First)