import { Link } from "react-router-dom";

function Nav() {
    return <>
        <nav className="navbar navbar-expand-sm bg-dark text-light">
            <ul className="navbar-nav">
                <li className="nav-item">
                    <Link className="nav-link text-white" href="#">Home</Link>
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
                <li className="nav-item">
                    <Link className="nav-link text-white" href="#">Sign in</Link>
                </li>
                <li className="nav-item">
                    <Link className="nav-link text-white" href="#">Sign up</Link>
                </li>
            </ul>

        </nav>
    </>
}
export default Nav;