use clap::Parser;
use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;

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

    let f = File::open(args.path).expect("The file cannot be read");
    let mut reader = BufReader::new(f);

    let mut line = String::new();
    loop {
        reader.read_line(&mut line).expect("[End of file]");
        if reader.buffer().is_empty() {
            break;
        }
        if line.contains(&args.pattern) {
            println!("{}", line)
        }
    }
}
