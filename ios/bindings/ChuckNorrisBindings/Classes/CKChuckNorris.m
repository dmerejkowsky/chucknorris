#import "CKChuckNorris.h"
#include "chucknorris.h"

@implementation CKChuckNorris

-(instancetype)init {
  self = [super init];
  self.ckPtr = chuck_norris_init();
  return self;
}

-(NSString *)getFact {
  const char* fact = chuck_norris_get_fact(self.ckPtr);
  return [NSString stringWithCString:fact encoding:NSUTF8StringEncoding];
}

+ (NSString*)versionString {
  return [NSString stringWithCString:chuck_norris_version() encoding:NSUTF8StringEncoding];
}
@end

