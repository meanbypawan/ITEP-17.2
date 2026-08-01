import React from "react";
function Fourth(){
    console.log("Fourth Rerender....")
    return <>
       <h1>Fourth Component...</h1>
    </>
}

export default React.memo(Fourth);