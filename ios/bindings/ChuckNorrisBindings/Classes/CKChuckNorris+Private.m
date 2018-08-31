#import "CKChuckNorris+Private.h"
#include "chucknorris.h"

@implementation CKChuckNorris (Private)

-(instancetype)createCkPtr  {
  self.ckPtr = chuck_norris_init();
  return self;
}

-(NSString*)getFactImpl {
  const char* fact = chuck_norris_get_fact(self.ckPtr);
  return [NSString stringWithCString:fact encoding:NSUTF8StringEncoding];
}

+(NSString*)versionStringImpl {
  char* version = chuck_norris_version();
  return [NSString stringWithCString:version encoding:NSUTF8StringEncoding];
}

@end
