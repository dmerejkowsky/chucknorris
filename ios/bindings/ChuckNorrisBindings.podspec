Pod::Spec.new do |s|
  s.name             = 'ChuckNorrisBindings'
  s.version          = '0.1.0'
  s.summary          = 'ChuckNorris as a iOS Objective-C library'
  s.description      = s.description
  s.homepage         = 'https://github.com/dmerejkowsky/chucknorris'
  s.license          = { :type => 'MIT', :file => 'LICENSE' }
  s.author           = { 'Dimitri Merejkowsky' => 'd.merej@gmail.com' }
  s.source           = { :git => 'https://github.com/dmerejkowsky/chucknorris.git', :tag => s.version.to_s }

  s.ios.deployment_target = '11.4'

  s.source_files = 'ChuckNorrisBindings/Classes/**/*'
  s.private_header_files = 'ChuckNorrisBindings/Classes/**/*+Private.h'

  s.pod_target_xcconfig = {
    'HEADER_SEARCH_PATHS' => '../../bindings/nativelibs/include'
  }

  s.libraries = ['c++', 'c++abi']
  s.vendored_libraries = Dir["nativelibs/universal/*.a"]

end
