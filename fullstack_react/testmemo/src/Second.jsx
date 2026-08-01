import React from "react"

function Second({message}){
    console.log("Second Rerender...")
    return <>
      <h1>Second component...{message}</h1>
    </>
}

const SecondMemoized = React.memo(Second)
export default SecondMemoized