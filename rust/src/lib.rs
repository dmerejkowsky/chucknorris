extern crate libc;
pub mod chucknorris;

pub use chucknorris::ChuckNorris;
use libc::c_char;
use std::ffi::CString;
use std::mem::transmute;

#[no_mangle]
pub extern "C" fn chuck_norris_init() -> *const ChuckNorris {
    let ck = unsafe { transmute(Box::new(ChuckNorris::new())) };
    ck
}

#[no_mangle]
pub extern "C" fn chuck_norris_deinit(ptr: *const ChuckNorris) {
    let ck: Box<ChuckNorris> = unsafe{ transmute(ptr) };
    drop(ck);
}

#[no_mangle]
pub extern "C" fn chuck_norris_get_fact(ptr: *const ChuckNorris) -> *mut c_char {
    let ck = unsafe { &*ptr };
    let fact = ck.get_fact();
    let c_str = CString::new(fact).unwrap();
    c_str.into_raw()
}
