use anyhow::{Context, Result};
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

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let args = CliArgs::parse();
    // println!("pattern: {:?}, path: {:?}", args.pattern, args.path);

    // let result = std::fs::read_to_string(args.path);
    // let content = match result {
    //     Ok(content) => content,
    //     Err(error) => return Err(error.into()),
    // };
    // or shortcut for above 2 expressions
    // let content = std::fs::read_to_string(args.path).unwrap();
    // same as
    // let content = std::fs::read_to_string(args.path)?;

    // attempt to provide more error context
    let content = std::fs::read_to_string(&args.path)
        .with_context(|| format!("The file cannot be read: `{}`", args.path.display()))?;

    println!("The file content:\n{}", content);

    for line in content.lines() {
        if line.contains(&args.pattern) {
            println!("{}", line)
        }
    }

    Ok(())
}
