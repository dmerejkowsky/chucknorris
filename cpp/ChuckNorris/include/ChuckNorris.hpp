#pragma once

#include <string>

struct sqlite3;

class ChuckNorris
{
  public:
    ChuckNorris();
    ~ChuckNorris();
    std::string getFact();


  private:
    sqlite3* _db;
};
