fn main() {
    let pattern = std::env::args().nth(1).expect("no pattern");
    let path = std::env::args().nth(2).expect("no file to search");

    println!("pattern: {:?}, path: {:?}", pattern, path);
}
