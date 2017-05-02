#ifndef PARSER_H
#define PARSER_H

#include <iostream>
#include <map>

#include <google/protobuf/compiler/importer.h>
#include <google/protobuf/io/zero_copy_stream.h>
#include <google/protobuf/dynamic_message.h>

#include <boost/filesystem.hpp>

#include <profanedb/protobuf/db.pb.h>
#include <profanedb/protobuf/options.pb.h>

using namespace google::protobuf;

namespace profanedb {
namespace storage {
    
// Given a Any message, Parser looks for the corresponding definition in .proto files,
// and generates a map with keys of nested messages
class Parser
{
public:
    Parser();
    ~Parser();
    
    // Generate a Dynamic Message out of an Any object, and return a set of dependent objects
    map<std::string, const Message &> ParseMessage(const Any & serializable);
    
    // Parse and object and return a set of dependent messages
    map<std::string, const Message &> ParseMessage(const Message & message);

private:
    io::ZeroCopyInputStream * inputStream;
    compiler::DiskSourceTree sourceTree;
    compiler::MultiFileErrorCollector * errCollector = new ErrorCollector();
    compiler::SourceTreeDescriptorDatabase * descriptorDb;
    DescriptorPool * pool;
    
    DynamicMessageFactory messageFactory;
    
    std::string FieldToString(const Message * container, const FieldDescriptor * fd);
    
    class ErrorCollector : public compiler::MultiFileErrorCollector {
    public:
        ErrorCollector();
        void AddError(const string & filename, int line, int column, const string & message) override;
        void AddWarning(const string & filename, int line, int column, const string & message) override;
    };
};

}
}

#endif // PARSER_H