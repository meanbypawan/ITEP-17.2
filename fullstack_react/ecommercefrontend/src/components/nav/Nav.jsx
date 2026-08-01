import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";
import { signOut } from "../../redux-config/UserSlice";

function Nav() {
    const {isLoggedIn} = useSelector((store)=>store.user)
    const dispatch = useDispatch()
    return <>
        <nav className="navbar navbar-expand-sm bg-dark text-light">
            <ul className="navbar-nav">
                <li className="nav-item">
                    <Link className="nav-link text-white" to="/">Home</Link>
                </li>
                <li className="nav-item">
                    <Link className="nav-link text-white" to="/">About us</Link>
                </li>
                <li className="nav-item">
                    <Link className="nav-link text-white" to="/">Categories</Link>
                </li>
                <li className="nav-item">
                    <Link className="nav-link text-white" to="/">Products</Link>
                </li>
                {!isLoggedIn && <li className="nav-item">
                    <Link className="nav-link text-white" to="/signin">Sign in</Link>
                </li>}
                {!isLoggedIn && <li className="nav-item">
                    <Link className="nav-link text-white" to="/signup">Sign up</Link>
                </li>}
                {isLoggedIn && <li className="nav-item">
                   <Link className="nav-link text-white" to="/view-cart">View cart</Link>
                </li>}
                {isLoggedIn && <li className="nav-item">
                    <button onClick={()=>{dispatch(signOut())}} className="nav-link btn btn-sm btn-outline-warning">Sign out</button>
                </li>}
            </ul>

        </nav>
    </>
}
export default Nav;