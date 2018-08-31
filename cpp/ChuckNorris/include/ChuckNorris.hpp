#pragma once

#include <string>

struct sqlite3;

class ChuckNorris
{
  public:
    ChuckNorris();
    ChuckNorris(ChuckNorris const&) = delete;
    ChuckNorris(ChuckNorris &&) = delete;
    ChuckNorris& operator=(ChuckNorris const&) = delete;
    ChuckNorris& operator=(ChuckNorris &&) = delete;

    static std::string version();


    std::string getFact();


  private:
    sqlite3* _db;
};
