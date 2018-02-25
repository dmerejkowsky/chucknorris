#pragma once

#include <string>

struct sqlite3;

class ChuckNorris
{
  public:
    ChuckNorris();
    std::string getFact();

    virtual ~ChuckNorris();

  private:
    sqlite3* _db;
};
