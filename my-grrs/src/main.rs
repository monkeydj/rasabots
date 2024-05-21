use clap::Parser;

#[derive(Parser)]
struct CliArgs {
    pattern: String,
    path: std::path::PathBuf,
}

fn main() {
    let args = CliArgs::parse();

    println!("pattern: {:?}, path: {:?}", args.pattern, args.path);
}
