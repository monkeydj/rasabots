use clap::Parser;

/// Search for a pattern in a file and display the lines that contain it.
#[derive(Parser)]
struct CliArgs {
    /// The pattern to look for in designated file
    #[arg(short = 'x', long)]
    pattern: String,
    /// The path to file to be searched
    #[arg(short = 'p', long)]
    path: std::path::PathBuf,
}

fn main() {
    let args = CliArgs::parse();
    // println!("pattern: {:?}, path: {:?}", args.pattern, args.path);

    let content = std::fs::read_to_string(args.path).expect("The file cannot be read");

    for line in content.lines() {
        if line.contains(&args.pattern) {
            println!("{}", line)
        }
    }
}
