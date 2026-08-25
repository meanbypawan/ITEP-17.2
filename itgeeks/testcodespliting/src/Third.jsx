
function withLogger(WrappedComponent){
    return function(props){
       console.log("Hello...........")
       /*
         extended code....
       */
       return <WrappedComponent/> // WrappedComponent is Hello Component...
    }
}
function Hello(){
    return <>
       <div>Hello...</div>
    </>
}
function Hi(){
    return <>
      <div>Hi...</div>
    </>
}
const HelloWithLogger = withLogger(Hello);
const HiWithLogger = withLogger(Hi)
export default HelloWithLogger