struct CliArgs {
    pattern: String,
    path: std::path::PathBuf,
}

fn main() {
    let pattern = std::env::args().nth(1).expect("no pattern");
    let path = std::env::args().nth(2).expect("no file to search");

    let args = CliArgs {
        pattern,
        path: std::path::PathBuf::from(path),
    };

    println!("pattern: {:?}, path: {:?}", args.pattern, args.path);
}
