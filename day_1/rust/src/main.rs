// use std::fs::File;
// use std::io::{self, BufRead};
// use std::path::Path;

// fn main() {
//     if let Ok(lines) = read_lines("./src/input.txt") {
//         for line in lines {
//             if let Ok(text) = line {
//                 println!("{}", text)
//             }
//         }
//     }
// }

// fn read_lines<P> (filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
// where P: AsRef<Path>, {
//     let file = File::open(filename)?;
//     Ok(io::BufReader::new(file).lines())
// }

use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    // Open the file in read-only mode
    let file = File::open("./src/input.txt").expect("Failed to open file");
    let reader = BufReader::new(file);

    // Create a vector to hold the groups of row elements
    let mut groups: Vec<Vec<i32>> = Vec::new();

    // Read each line from the file
    for line in reader.lines() {
        let line = line.expect("Failed to read line");

        // If the line is empty, add a new group to the vector
        if line.is_empty() {
            groups.push(Vec::new());
        } else {
            // Otherwise, split the line on whitespace and parse each element as an integer
            let row_elements: Vec<i32> = line
                .split_whitespace()
                .map(|s| s.parse().expect("Failed to parse integer"))
                .collect();

            // Add the row elements to the current group
            if let Some(group) = groups.last_mut() {
                group.extend(row_elements);
            }
        }
    }

    // Find the maximum sum of elements in the groups of row elements
    let mut max_sum = 0;
    for group in groups {
        let sum: i32 = group.iter().sum();
        if sum > max_sum {
            max_sum = sum;
        }
    }

    println!("The maximum sum of elements is: {}", max_sum);
}