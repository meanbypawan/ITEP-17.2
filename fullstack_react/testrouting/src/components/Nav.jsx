import { Link } from "react-router-dom"

const Nav = ()=>{
    return <>
      <div className="container-fluid d-flex justify-content-around align-items-center p-3">
        <Link to="/">Home</Link>
        <Link to="/about">About us</Link>
        <Link to="/contact">Contact us</Link>
        <Link to="/use-effect">useEffect</Link>
        <Link to="/quotes">Quotes</Link>
      </div>
    </>
}

export default Nav