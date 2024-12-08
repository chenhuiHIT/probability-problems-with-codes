use rand::Rng;

fn run(repeat_nums: usize) {
    let mut switch_win = 0;
    let mut no_switch_win = 0;

    for _ in 0..repeat_nums {
        let position = rand::thread_rng().gen_range(0..3); // Randomly choose a position (0, 1, or 2)
        if position == 0 {
            no_switch_win += 1;
        } else {
            switch_win += 1;
        }
    }

    println!("Switch win ratio: {:.6}", switch_win as f64 / repeat_nums as f64);
    println!("No switch win ratio: {:.6}", no_switch_win as f64 / repeat_nums as f64);
}

fn main() {
    let test_num = 1_000_000;
    run(test_num);
}
