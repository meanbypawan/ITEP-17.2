import { Component } from "react";

class Banner extends Component{
    render(){
        return <>
                <section className="slider_section position-relative">
        <div className="slider_bg_box">
          <img src="images/slider-bg.jpg" alt="" />
        </div>
        <div className="slider_bg"></div>
        <div className="container">
          <div className="col-md-9 col-lg-8">
            <div className="detail-box">
              <h1>
                Best Jewellery
                <br /> Collection
              </h1>
              <p>
                It is a long established fact that a reader will be distracted by the readable content of a page when
                looking at its layout. The point of using Lorem
              </p>
              <div>
                <a href="" className="slider-link">
                  Shop Now
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>
        </>
    }
}
export default Banner;