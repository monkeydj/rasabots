use clap::Parser;

/// Search for a pattern in a file and display the lines that contain it.
#[derive(Parser)]
struct CliArgs {
    /// The pattern to look for in designated file
    #[arg(short = 's', long)]
    pattern: String,
    /// The path to file to be searched
    #[arg(short = 'f', long)]
    path: std::path::PathBuf,
}

fn main() {
    let args = CliArgs::parse();
    // println!("pattern: {:?}, path: {:?}", args.pattern, args.path);

    let result = std::fs::read_to_string(args.path);
    match result {
        Ok(content) => {
            println!("The file content:\n{}", content);
        }
        Err(error) => {
            println!("The file cannot be read: {}", error);
        }
    }

    // for line in content.lines() {
    //     if line.contains(&args.pattern) {
    //         println!("{}", line)
    //     }
    // }
}
