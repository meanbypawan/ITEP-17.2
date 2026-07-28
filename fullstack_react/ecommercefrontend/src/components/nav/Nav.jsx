import { useSelector } from "react-redux";
import { Link } from "react-router-dom";

function Nav() {
    const {isLoggedIn} = useSelector((store)=>store.user)
    return <>
        <nav className="navbar navbar-expand-sm bg-dark text-light">
            <ul className="navbar-nav">
                <li className="nav-item">
                    <Link className="nav-link text-white" href="/">Home</Link>
                </li>
                <li className="nav-item">
                    <Link className="nav-link text-white" href="#">About us</Link>
                </li>
                <li className="nav-item">
                    <Link className="nav-link text-white" href="#">Categories</Link>
                </li>
                <li className="nav-item">
                    <Link className="nav-link text-white" href="#">Products</Link>
                </li>
                {!isLoggedIn && <li className="nav-item">
                    <Link className="nav-link text-white" to="/signin">Sign in</Link>
                </li>}
                {!isLoggedIn && <li className="nav-item">
                    <Link className="nav-link text-white" to="/signup">Sign up</Link>
                </li>}
                {isLoggedIn && <li className="nav-item">
                    <Link className="nav-link text-white" to="">Sign out</Link>
                </li>}
            </ul>

        </nav>
    </>
}
export default Nav;