use assert_cmd::prelude::*; // Add methods on commands
use predicates::prelude::*; // for writing assertions
use std::process::Command; // executing command

#[test]
pub fn file_doesnt_exist() -> Result<(), Box<dyn std::error::Error>> {
    let mut cmd = Command::cargo_bin("my_grrs")?;

    cmd.arg("path").arg("ghost/file");
    cmd.assert()
        .failure()
        .stderr(predicate::str::contains("The file cannot be read"));

    Ok(());
}
