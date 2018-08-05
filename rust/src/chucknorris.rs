extern crate sqlite;

pub struct ChuckNorris {
    connection: sqlite::Connection,
}

impl ChuckNorris {
    fn facts() -> Vec<&'static str> {
        vec![
          "Chuck Norris was bitten by a cobra and after five days of excruciating pain... the cobra died.",
          "The easiest way to determine Chuck Norris's age is to cut him in half and count the rings.",
          "Chuck Norris doesn't dial the wrong number. You answered the wrong phone.",
          "Chuck Norris knows Victoria's secret",
          "If Chuck Norris was a Spartan in the movie 300, the movie would be called 1",
          "Chuck Norris can kill two stones with one bird.",
          "Chuck Norris can slam a revolving door.",
          "There are no weapons of mass destruction in Iraq, Chuck Norris lives in Oklahoma.",
          "If, by some incredible space-time paradox, Chuck Norris would ever fight himself, he'd win. Period.",
          "Chuck Norris sleeps with a pillow under his gun.",
          "Chuck Norris threw a grenade and killed 50 people, then it exploded.",
          "Chuck Norris counted to infinity. Twice.",
          "Giraffes were created when Chuck Norris uppercutted a horse.",
          "When a zombie apocalypse starts, Chuck Norris doesn't try to survive. The zombies do."
      ]
    }

    pub fn new() -> ChuckNorris {
        let connection = sqlite::open(":memory:").unwrap();

        connection
            .execute("CREATE TABLE chucknorris(id PRIMARY_KEY, fact TEXT)")
            .unwrap();

        let facts = ChuckNorris::facts();
        for fact in facts.iter() {
            let mut statement = connection
                .prepare("INSERT INTO chucknorris (fact) VALUES (?)")
                .unwrap();
            statement.bind(1, *fact).unwrap();
            statement.next().unwrap();
        }
        ChuckNorris { connection }
    }

    pub fn get_fact(&self) -> String {
        let mut statement = self
            .connection
            .prepare(
                "
            SELECT fact FROM chucknorris ORDER BY RANDOM() LIMIT 1;",
            )
            .unwrap();
        if let sqlite::State::Row = statement.next().unwrap() {
            let fact = statement.read::<String>(0).unwrap();
            return fact;
        }
        "".to_string()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_has_facts() {
        let facts = ChuckNorris::facts();
        assert_ne!(facts.len(), 0);
    }

    #[test]
    fn get_fact() {
        let chuck_norris = ChuckNorris::new();
        let fact = chuck_norris.get_fact();
        assert_ne!(fact.len(), 0);
    }
}
